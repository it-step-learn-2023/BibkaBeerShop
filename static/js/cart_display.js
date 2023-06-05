$(document).ready(() => {

    console.log('cart-display.js -> Start');
    const userId = $('#user-id').val();

    $.ajax({
        url: "/orders/ajax_cart_display",
        data: `uid=${userId}`,
        success: (response) => {
            $('#cart-count').text(response.count);
            $('#_count').text(`Товарів у кошику: ${response.count} шт`);
            $('#_total').text(`ВАРТІСТЬ: ${response.total} грн`);
        }
    });
    

})