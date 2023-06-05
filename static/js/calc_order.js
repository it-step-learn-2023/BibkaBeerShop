const doCalculate = () => {
    // 1
    console.log('doCalculate() - Work');

    // 2
    let checkedBoxes = $('.check:checked');
    let totalPrice = 0;
    let selOrderIds = "";

    // 3
    for (let box of checkedBoxes) {
        let parentRow = $(box).parent().parent();
        let currentPrice = parseFloat($(parentRow).find('td.price-cell').text());
        let currentCount = parseFloat($(parentRow).find('td.count-cell').find('input').val());
        totalPrice += currentPrice * currentCount;
        selOrderIds += $(parentRow).find('td.id-cell').text() + ',';
    }
    selOrderIds += totalPrice;

    // 4
    console.log(`totalPrice: ${totalPrice}`);
    console.log(`selOrdersIds: ${selOrderIds}`);
    $('#total').text(`${totalPrice.toFixed(2)} грн`);
    $('#bill-btn').attr('href', `/orders/bill/${selOrderIds}`);
    if (totalPrice == 0) {
        $('#bill-btn').fadeOut(1000);
    } else {
        $('#bill-btn').fadeIn(1000);
    }
};

$(document).ready(() => {

    // 1
    console.log('calc_order.js -> Start!')
    doCalculate();

    // 2
    $('.check').click((event) => {
        console.log('input.check -> click');
        doCalculate();
    })
    // HT
    $('.count').click((event) => {
        console.log("count click")
        doCalculate()
    })
    $('.count').blur((event) => {
        console.log("count click")
        doCalculate()
    })
});