from django.contrib import admin
from django.urls import path
from staff_app.views import *
from staff_app.utils import *

urlpatterns = [
    path('dashboard', staff_dashboard),
    path('show', staff_show),
    path('productcategories', staff_product_categories),
    path('', staff_login),
    path('productcategories', staff_product_categories),
    path('staff_pv', staff_pv_wallet),
    path('deleteproductcategory', staff_delete_product_category),
    path('editproductcategory', staff_edit_product_category),
    path('productsubcategories', staff_product_sub_categories),
    path('editproductsubcategory', staff_edit_product_sub_categories),
    path('deleteproductsubcategory', staff_delete_product_sub_category),
    path('productsubsubcategories', staff_product_sub_sub_categories),
    path('editproductsubsubcategory', staff_edit_product_sub_sub_categories),
    path('deleteproductsubsubcategory', staff_delete_product_sub_sub_category),
    path('kycrequests', staff_kyc_requests),
    path('activatevendor', staff_activate_vendor),
    path('point/', staff_point_value),
    path('createlink', staff_create_link),
    path('generatelink-left', staff_generate_link_left),
    path('generatelink-right', staff_generate_link_right),
    path('undertrees', staff_under_trees),
    path('binary/genealogyTree', genealogyTree_binary),
    path('level/genealogyTree', genealogyTree_level),
    path('level/underlevel', staff_under_trees_level),
    path('deliverycharges', staff_delivery_charges),
    path('vendor-list', staff_vendor_list),
    path('activate_isavplvendor', staff_is_activate_approved_avpl_vendor),
    path('activateisavplvendor', staff_activate_approved_avpl_vendor),
    path('deactivate_isavplvendor', staff_is_deactivate_approved_avpl_vendor),
    path('vendorprofile', staff_vendor_profile),
    path('paymentinfo', staff_payment_info),
    path('orders', staff_orders),
    path('setpvpair', staff_pvpairvalue),
    path('leadershipbonus', staff_leadership_bonus_set),
    path('housefund', staff_house_fund_set),
    path('carfund', staff_car_fund_set),
    path('directorshipfund', staff_directorship_fund_set),
    path('travelfund', staff_travel_fund_set),
    path('sendmoney', staff_send_money),
    path('withdraw', staff_withdraw),
    path('changewithdrawstatus', staff_change_withdraw_status),
    path('query', staff_query),
    path('queryresult', staff_query_result),
    path('changequerystatus', staff_change_query_status),
    path('setpvconversion', staff_set_pv_conversion),
    
    path('product', staff_product),
    path('productapproval', staff_product_approval),
    path('all-products', staff_product_list),
    path('productbasicedit', staff_product_basic_edit),
    path('deleteproductimage', staff_delete_product_image),
    path('deleteproductvariant', staff_delete_product_variant),
    path('outofstock', staff_product_out_of_stock),
    path('activateproduct', staff_activate_product),
    path('sendqueryreply', staff_query_send_reply),
    path('wallet_details', wallet_details),
    
    path('tax', staff_taxation),
    path('users', staff_users),
    path('users/delete', staff_users_delete),
    #path for User commission for refered vendor
    path('uservendorcommission', user_vendor_commission),
    path('settings/', staff_level_settings),
    path('fetchgroups/', staff_fetch_groups),
    path('edit/group/', staff_edit_group),
    path('level/settings/', staff_level_settings_level_plan),
    path('level/fetchgroups/', staff_fetch_groups_level),
    path('level/edit/group/', staff_edit_group_level),
    path('minmumcartvalue/', staff_min_cart_value),
    path('billing/config/', staff_billing_config),
    path('product/reject/', staff_reject_product),
    path('product/update/', staff_update_product),
    path('gst_log/', staff_gst_log),
    path('tds_log/', staff_tds_withdraw),
    path('contact', contact),
    path('terms', terms),
    path('privacy', privacy),
    path('about-us', staff_about_us),
    path('gallery', staff_gallery),
    path('blog', staff_blog),
    path('banner', staff_banner),
    path('direct-referal', staff_direct_referal),

    path('subscription-pack',staff_subscription_pack),
    path('userSubscriptionRequest',userSubscriptionRequest_staff),

    path('balanacetransfers', staffbalanacetransfer, name='balanacetransfers'),
    path('otpvalidations', transfer_amount_staff, name='otpvalidations'),

    path('vendor-commission-wallet', staff_vendor_commission_wallet),
    path('staff-vendor-commission-wallet/<int:id>',staff_vendor_commission_wallet_details, name='staff-vendor-commission-wallet'),
    path('activate_is_commission_wallet', staff_activate_is_commission_wallet_vendor),
    path('deactivate_is_commission_wallet', staff_deactivate_is_commission_wallet_vendor),

   


    
]