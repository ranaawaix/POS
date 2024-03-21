$(document).ready(function () {
    $('.product').each(function () {
        $(this).on('click', function (e) {
            e.preventDefault();
            let prod_id = $(this).data('pid');
            let user_id = $(this).data('user');
            let register_id = $(this).data('register_id');
            let sale_id = $('#saleId').data('sid');
            let csrf = $("input[name=csrfmiddlewaretoken]").val();
            console.log(sale_id, prod_id, user_id, register_id);
            let my_data = {}
            if (sale_id) {
                my_data = {
                    prod_id: prod_id,
                    sale_id: sale_id,
                    user_id: user_id,
                    register_id: register_id,
                    csrfmiddlewaretoken: csrf
                }
            } else {
                my_data = {prod_id: prod_id, user_id: user_id, register_id: register_id, csrfmiddlewaretoken: csrf}
            }
            var url = $(this).data('url');
            console.log(my_data, url);
            $.ajax({
                url: url, method: 'POST', data: my_data, success: function (rsp) {
                    console.log(rsp)
                    $('.billing').html(rsp);
                    $('.billing .table-bordered tr').each(function () {
                        $(this).find('#sale_item_quantity').each(function () {
                            $(this).on('blur', function () {
                                let quantity = $(this).val();
                                let sale_id = $('#saleId').data('sid');
                                let price = $(this).closest('tr').find('.saleitem_price').text();
                                let result = quantity * price;
                                $(this).closest('tr').find('.saleitem_subtotal').text(result);
                                let subtotal = result.toFixed();
                                let eurl = $('#sale_item_quantity').data('eurl');
                                let my_data = {
                                    prod_id: prod_id,
                                    sale_id: sale_id,
                                    user_id: user_id,
                                    register_id: register_id,
                                    quantity: quantity,
                                    price: price,
                                    subtotal: subtotal,
                                    csrfmiddlewaretoken: csrf
                                }
                                console.log(my_data);
                                $.ajax({
                                    url: eurl, method: 'POST', data: my_data, success: function (rsp) {
                                        console.log(rsp);
                                        $('.billing').html(rsp);
                                    }, error: function (xhr, status, error) {
                                        console.error(error);
                                    }
                                });
                            });
                        })
                    })
                }
            })
        })
    })

    $('.holdForm').on('submit', function (e) {
        e.preventDefault();
        let sale_id = $('#SaleID').data('slid');
        let note = $(this).find('#id_reference_note').val();
        let csrf = $("input[name=csrfmiddlewaretoken]").val();
        let url = $('#SaleID').data('url');
        let rurl = $('#SaleID').data('rurl');
        console.log(sale_id, note);
        let my_data = {sale_id: sale_id, note: note, csrfmiddlewaretoken: csrf}
        $.ajax({
            url: url, method: 'POST', data: my_data, success: function (data) {
                if (data.status === 'Saved') {
                    $('#modalHold').modal('show');
                    $("#msg strong").text("Order Held successfully");
                    $("#msg").show();
                    setTimeout(function () {
                        $('#modalHold').modal('hide');
                    }, 5000);
                    $('.modal-backdrop').removeClass('modal-backdrop fade');
                    data.success(window.location.href = rurl)
                } else if (data.status === 0) {
                    $('#modalHold').modal('show');
                    $("#msgfail strong").text("Unable to Hold order");
                    $('#msgfail').show();
                    setTimeout(function () {
                        $('#modalHold').modal('hide');
                    }, 5000);
                    $('.modal-backdrop').removeClass('modal-backdrop fade');
                }
            }
        });
    });
    $('.customerForm').on('submit', function (e) {
        e.preventDefault();
        let name = $(this).find('#id_name').val();
        let email = $(this).find('#id_email').val();
        let phone = $(this).find('#id_phone').val();
        let custom_1 = $(this).find('#id_customer_custom_field_1').val();
        let custom_2 = $(this).find('#id_customer_custom_field_2').val();
        let csrf = $("input[name=csrfmiddlewaretoken]").val();
        let sale_id = $('#SaleId').data('saleid');
        let url = $('#SaleId').data('url');
        console.log(name, email, phone, custom_1, custom_2, sale_id);
        my_data = {
            sale_id: sale_id,
            name: name,
            email: email,
            phone: phone,
            custom_1: custom_1,
            custom_2: custom_2,
            csrfmiddlewaretoken: csrf
        }
        $.ajax({
            url: url, method: 'POST', data: my_data, success: function (rsp) {
                let customer_id = rsp.cust_id;
                if (rsp.status === 'Saved') {
                    $('#modalCustomer').modal('show');
                    $("#msgc strong").text("Added the customer successfully");
                    $("#msgc").show();
                    setTimeout(function () {
                        $('#modalCustomer').modal('hide');
                    }, 5000);
                    $('.modal-backdrop').removeClass('modal-backdrop fade');
                    if (customer_id) {
                        console.log(customer_id);
                        $('#id_customer').val(customer_id);
                    }
                } else if (rsp.status === 0) {
                    $('#modalCustomer').modal('show');
                    $("#msgcfail strong").text("Unable to add customer");
                    $('#msgcfail').show();
                    setTimeout(function () {
                        $('#modalCustomer').modal('hide');
                    }, 5000);
                    $('.modal-backdrop').removeClass('modal-backdrop fade');
                }
            }
        });
    });
    $(document).on('submit', '#paymentForm', function (e) {
        debugger;
        e.preventDefault();
        let sale_id = $('#saleId').data('sid');
        let sale_input = $('#sale_id');
        let url = sale_input.data('url');
        let rurl = sale_input.data('rurl');
        let reg_id = sale_input.data('regid');
        let note = $(this).find('#id_note').val();
        let amount = $(this).find('#id_amount').val();
        let payment_by = $(this).find('#id_payment_by').val();
        let payment_note = $(this).find('#id_payment_note').val();
        let csrf = $("input[name=csrfmiddlewaretoken]").val();
        console.log(note, amount, payment_by, payment_note, sale_id, reg_id);
        let my_data = {
            sale_id: sale_id,
            reg_id: reg_id,
            note: note,
            amount: amount,
            payment_by: payment_by,
            payment_note: payment_note,
            csrfmiddlewaretoken: csrf
        }
        $.ajax({
            url: url, method: 'POST', data: my_data, success: function (rsp) {
                if (rsp.status === 'Saved') {
                    $('#modalPayment').modal('show');
                    $("#msgp strong").text("Payment submitted successfully");
                    $("#msgp").show();
                    setTimeout(function () {
                        $('#modalPayment').modal('hide');
                    }, 5000);
                    $('.modal-backdrop').removeClass('modal-backdrop fade');
                    rsp.success(window.location.href = rurl);
                } else if (rsp.status === 0) {
                    $('#modalPayment').modal('show');
                    $("#msgpfail strong").text("Unable to submit payment");
                    $('#msgpfail').show();
                    setTimeout(function () {
                        $('#modalPayment').modal('hide');
                    }, 5000);
                    $('.modal-backdrop').removeClass('modal-backdrop fade');
                }
            }
        });
    });
    $(".btn-group-vertical button").on("click", function () {
        let buttonText = $(this).text();
        let total_paying = $(this).val();
        let total_payable = $('#totalPayable').data('tp');
        let balance = total_paying - total_payable;
        console.log(total_paying, total_payable, balance);
        $('#totalPaying').html(buttonText);
        $('#id_amount').val(total_payable);
        $('#balance').html(balance);
    });
    $("#clear").on("click", function () {
        $('#totalPaying').html(0);
        $('#id_amount').val(0);
    });
    $(document).ready(function () {
        $('#delete_saleitem a').on('click', function (e) {
            e.preventDefault();
            let sale_id = $('#saleId').data('sid');
            let saleitem_id = $(this).data('sp');
            let url = $(this).data('url');
            let csrf = $("input[name=csrfmiddlewaretoken]").val();
            console.log(sale_id, saleitem_id);
            let my_data = {sale_id: sale_id, saleitem_id: saleitem_id, csrfmiddlewaretoken: csrf}
            $.ajax({
                url: url, method: 'POST', data: my_data, success: function (rsp) {
                    console.log(rsp)
                    $('.billing').html(rsp);
                    Swal.fire({
                        icon: "success",
                        title: "Item Deleted Successfully",
                        showConfirmButton: false,
                        timer: 1500
                    });
                }
            })
        })
    })
});
