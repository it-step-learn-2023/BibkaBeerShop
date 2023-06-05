$(document).ready(() => {

    console.log('cart.js -> Start');

    $('#catalog').on('click', '#add-to-cart-btn', (event) => {
        // 1
        console.log('add-btn -> Click');
        const userId = $('#user-id').val();
        console.log('User-ID:' + userId);
        let productCount = $('#count-1').val()

        // 2
        if (userId == 'None') {
            alert('Для використання кошику авторизуйтесь!');
        } else {
            // 3
            let productId = $(event.target).prev().prev().val();
            console.log('ProductID:' + productId);
            console.log('ProductCoutn:' + productCount);

            // 4
            $.ajax({
                url: '/orders/ajax_cart',
                data: `uid=${userId}&pid=${productId}&cid=${productCount}`,
                success: (respose) => {
                    console.log(respose);
                    alert('Товар додан до кошику!')
                    $('#cart-count').text(respose.count);
                    $('#_count').text(`Товарів у кошику: ${respose.count} шт`);
                    $('#_total').text(`ВАРТІСТЬ: ${respose.total} грн`);
                }
            });
        }
    });
});
