from django.shortcuts import render
from django.views import generic
from .models import Sales
from .forms import SalesSearchForm
from reports.forms import ReportForm
import pandas as pd
from .utils import get_customer_from_id,\
    get_salesman_from_id, get_chart
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def home_view(request):
    search_form = SalesSearchForm(request.POST or None)
    report_form = ReportForm()

    sales_df = None
    position_df = None
    merged_df = None
    df = None
    chart = None
    no_data = None
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        results_by = request.POST.get('results_by')

        sale_qs = Sales.objects.filter(
            created__date__lte=date_to,
            created__date__gte=date_from
        )
        if len(sale_qs):
            sales_df = pd.DataFrame(sale_qs.values())
            sales_df['customer_id'] = sales_df['customer_id'].apply(
                get_customer_from_id
            )
            sales_df['salesman_id'] = sales_df['salesman_id'].apply(
                get_salesman_from_id
            )
            sales_df['created'] = sales_df['created'].apply(
                lambda x: x.strftime('%d.%m.%Y')
            )
            sales_df['updated'] = sales_df['updated'].apply(
                lambda x: x.strftime('%d.%m.%Y')
            )
            sales_df.rename({
                'id': 'sales-id',
                'customer_id': 'customer',
                'salesman_id': 'salesman',
                'position_id': 'position',

            }, axis=1, inplace=True)

            position_data = []
            for sale in sale_qs:
                for pos in sale.get_positions():
                    obj = {
                        'position_id': pos.id,
                        'product': pos.product.name,
                        'quantity': pos.quantity,
                        'price': pos.price,
                        'sales_id': pos.get_sales_id()
                    }
                    position_data.append(obj)

            position_df = pd.DataFrame(position_data)
            position_df.rename({
                'position_id': 'position',
                'sales_id': 'sales-id',
            }, axis=1, inplace=True)

            merged_df = pd.merge(sales_df, position_df, on='sales-id')

            df = merged_df.groupby(
                'transaction_id',
                as_index=False
            )['price'].agg('sum')

            chart = get_chart(chart_type, sales_df, results_by)
            sales_df = sales_df.to_html()
            position_df = position_df.to_html()
            merged_df = merged_df.to_html()
            df = df.to_html()
        else:
            no_data = 'No data is available in this date range.'

    context = {
        'search_form': search_form,
        'report_form': report_form,
        'sales_df': sales_df,
        'position_df': position_df,
        'merged_df': merged_df,
        'df': df,
        'chart': chart,
        'no_data': no_data,
    }
    return render(request, 'sales/home.html', context)


class SaleListView(LoginRequiredMixin, generic.ListView):
    model = Sales
    template_name = 'sales/main.html'
    context_object_name = 'qs'


# def sale_list_view(request):
#     qs = Sales.objects.all()
#     return render(request, 'sales/main.html', {'qs': qs})


class SaleDetailView(LoginRequiredMixin, generic.DetailView):
    model = Sales
    template_name = 'sales/detail.html'

# def sale_detail_view(request, **kwargs):
#     pk = kwargs.get('pk')
#     obj = Sales.objects.get(pk=pk)
#     return render(request, 'sales/detail.html', {'object': obj})
