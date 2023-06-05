$(document).ready(() => {

    console.log('del_product.js -> Start');
    
    $('.del-btn').click(event => {
        console.log('del-btn -> Click')

        let productId = $(event.target).prev().val();
        console.log(`productId: ${productId}`)

        $.ajax({
            url: '/catalog/ajax_del_product',
            data: `product_id=${productId}`,
            success: (response) => {
                console.log(response);
                alert(response.result);
                window.location = '/catalog';
            }
        })
    });

});
