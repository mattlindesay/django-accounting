from django.urls import include, path
from . import views

app_name = 'books'

urlpatterns = [
#    path('', views.DashboardView.as_view(), name="dashboard"),

    # Organizations
    path('organization/', views.OrganizationListView.as_view(), name="organization-list"),
    path('organization/selector/', views.OrganizationSelectorView.as_view(), name="organization-selector"),
    path('organization/create/', views.OrganizationCreateView.as_view(), name="organization-create"),
    path('organization/<int:pk>/edit/', views.OrganizationUpdateView.as_view(), name="organization-edit"),
    path('organization/<int:pk>/detail/', views.OrganizationDetailView.as_view(), name="organization-detail"),
    path('organization/<int:pk>/select/', views.OrganizationSelectionView.as_view(), name="organization-select"),

    # Tax Rates
    path('tax_rates/', views.TaxRateListView.as_view(), name="tax_rate-list"),
    path('tax_rates/create/', views.TaxRateCreateView.as_view(), name="tax_rate-create"),
    path('tax_rates/<int:pk>/edit/', views.TaxRateUpdateView.as_view(), name="tax_rate-edit"),
    path('tax_rates/<int:pk>/delete/', views.TaxRateDeleteView.as_view(), name="tax_rate-delete"),

    # Estimates
    path('estimate/', views.EstimateListView.as_view(), name="estimate-list"),
    path('estimate/create/', views.EstimateCreateView.as_view(), name="estimate-create"),
    path('estimate/<int:pk>/edit/', views.EstimateUpdateView.as_view(), name="estimate-edit"),
    path('estimate/<int:pk>/delete/', views.EstimateDeleteView.as_view(), name="estimate-delete"),
    path('estimate/<int:pk>/detail/', views.EstimateDetailView.as_view(), name="estimate-detail"),

    # Invoices
    path('invoice/', views.InvoiceListView.as_view(), name="invoice-list"),
    path('invoice/create/', views.InvoiceCreateView.as_view(), name="invoice-create"),
    path('invoice/<int:pk>/edit/', views.InvoiceUpdateView.as_view(), name="invoice-edit"),
    path('invoice/<int:pk>/delete/', views.InvoiceDeleteView.as_view(), name="invoice-delete"),
    path('invoice/<int:pk>/detail/', views.InvoiceDetailView.as_view(), name="invoice-detail"),

    # Bills
    path('bill/', views.BillListView.as_view(), name="bill-list"),
    path('bill/create/', views.BillCreateView.as_view(), name="bill-create"),
    path('bill/<int:pk>/edit/', views.BillUpdateView.as_view(), name="bill-edit"),
    path('bill/<int:pk>/delete/', views.BillDeleteView.as_view(), name="bill-delete"),
    path('bill/<int:pk>/detail/', views.BillDetailView.as_view(), name="bill-detail"),

    # ExpenseClaims
    path('expense-claim/', views.ExpenseClaimListView.as_view(), name="expense_claim-list"),
    path('expense-claim/create/', views.ExpenseClaimCreateView.as_view(), name="expense_claim-create"),
    path('expense-claim/<int:pk>/edit/', views.ExpenseClaimUpdateView.as_view(), name="expense_claim-edit"),
    path('expense-claim/<int:pk>/delete/', views.ExpenseClaimDeleteView.as_view(), name="expense_claim-delete"),
    path('expense-claim/<int:pk>/detail/', views.ExpenseClaimDetailView.as_view(), name="expense_claim-detail"),

    # Payments
    path('payment/<int:pk>/edit/', views.PaymentUpdateView.as_view(), name="payment-edit"),
    path('payment/<int:pk>/delete/', views.PaymentDeleteView.as_view(), name="payment-delete"),
]
