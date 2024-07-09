import json
from datetime import date
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, FloatField, F
from django.db.models.functions import Coalesce
from django.shortcuts import render
from customers.models import Customer
from products.models import Product, Category
from sales.models import Sale,SaleDetail


@login_required(login_url="/accounts/login/")
def index(request):
    today = date.today()

    year = today.year
    monthly_earnings = []
    total_profit=0

    # Calculate earnings per month
    for month in range(1, 13):
        earning = Sale.objects.filter(date_added__year=year, date_added__month=month).aggregate(
            total_variable=Coalesce(Sum(F('grand_total')), 0.0, output_field=FloatField())).get('total_variable')
        monthly_earnings.append(earning)

    # Calculate annual earnings
    annual_earnings = Sale.objects.filter(date_added__year=year).aggregate(total_variable=Coalesce(
        Sum(F('grand_total')), 0.0, output_field=FloatField())).get('total_variable')
    annual_earnings = format(annual_earnings, '.2f')

    # calculate profit

    total_profit = SaleDetail.objects.annotate(
        profit=F('product__selling_price') - F('product__price')).aggregate(
        total_profit=Coalesce(Sum(F('profit') * F('quantity')), 0.0, output_field=FloatField())).get('total_profit')
    total_profit = format(total_profit, '.2f')
    print(total_profit)

    #calculate annual discounts

    total_discounts = Sale.objects.filter(date_added__year=year).aggregate(total_variable=Coalesce(
        Sum(F('tax_amount')), 0.0, output_field=FloatField())).get('total_variable')
    total_discounts = format(total_discounts, '.2f')

    # AVG per month
    avg_month = format(sum(monthly_earnings), '.2f')

    # Top-selling products
    top_products = Product.objects.annotate(quantity_sum=Sum(
        'saledetail__quantity')).order_by('-quantity_sum')[:10]

    top_products_names = []
    top_products_quantity = []

    for p in top_products:
        top_products_names.append(p.name)
        top_products_quantity.append(p.quantity_sum)

    print(top_products_names)
    print(top_products_quantity)

    context = {
        "active_icon": "dashboard",
        "products": Product.objects.all().count(),
        "categories": Category.objects.all().count(),
        "annual_earnings": annual_earnings,
        "total_profit": total_profit,
        "total_discounts": total_discounts,
        "customers": Customer.objects.all().count,
        "monthly_earnings": json.dumps(monthly_earnings),
        "avg_month": avg_month,
        "top_products_names": json.dumps(top_products_names),
        "top_products_names_list": top_products_names,
        "top_products_quantity": json.dumps(top_products_quantity),
    }
    return render(request, "pos/index.html", context)
