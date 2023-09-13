$(document).ready(function () {
    $('.increment-btn').click(function(e)  {
        e.preventDefault();
        var inc_value = $(this).closest('.pd_data').find('.qty-input').val();
        var prd_qty = $(this).closest('.pd_data').find('.prd_qty').val();
        var value = parseInt(inc_value,prd_qty);
        // value =isNaN(value) ? 0 : value;
        print(prd_qty)
        if (value<prd_qty) {
            value++;
            $(this).closest('.pd_data').find('.qty-input').val(value);
        }
    });
    $('.decrement-btn').click(function(e)  {
        e.preventDefault();
        var dec_value = $(this).closest('.pd_data').find('.qty-input').val();
        var value = parseInt(dec_value,10);
        // value =isNaN(value) ? 0 : value;
        if (value>1) {
            value--;
            $(this).closest('.pd_data').find('.qty-input').val(value);
        }
    });
});