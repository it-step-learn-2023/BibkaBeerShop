const doCountProducts = () => {
    console.log("count click")
    const userId = $('#user-id').val();
    console.log('User-ID:' + userId);
        
    let productCount = $(event.target).val();
    let productId = $(event.target).next().val();
    let orderId = $(event.target).next().next().val()
        
    console.log('----------------------------------')
    console.log(orderId)
    console.log('ProductID:' + productId);
    console.log('ProductCoutn:' + productCount);
    
    $.ajax({
        url: '/orders/ajax_cart_count',
        data: `uid=${userId}&pid=${productId}&cid=${productCount}&oidt${orderId}`,
        success: (respose) => {
            console.log(respose);
        }   
    });

}

$(document).ready(() => {

    console.log('count_cart.js -> Start');

    $('.count').click((event) => {
        doCountProducts();
    })
    
    $('.count').blur((event) => {
        doCountProducts();
    });
});
