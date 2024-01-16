$(document).ready(function () {
    $('.increment-btn').click(function(e)  {
        e.preventDefault();
        var dec_value = $(this).closest('.pd_data').find('.qty-input').val();
        var product_qty = $(this).closest('.pd_data').find('.prd_quantity').val();
        var value = parseInt(dec_value,10);
        // value =isNaN(value) ? 0 : value;
        if (value<product_qty) {
            value++;
            $(this).closest('.pd_data').find('.qty-input').val(value);
        }
        // 
        // value =isNaN(value) ? 0 : value;
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