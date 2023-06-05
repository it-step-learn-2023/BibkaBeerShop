$(document).ready(() => {

    console.log('del_order.js -> Start');
    
    $('.del-btn').click(event => {
        console.log('del-btn -> Click')

        let orderId = $(event.target).prev().val();
        console.log(`orderId: ${orderId}`)

        $.ajax({
            url: '/orders/ajax_del_order',
            data: `order_id=${orderId}`,
            success: (response) => {
                console.log(response);
                alert(response.result);
                window.location = '/orders';
            }
        })
    });

});
