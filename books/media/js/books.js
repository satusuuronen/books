function showInformation(button) {
    var information = $(button).parent().parent().find('.information');
    if (!($(information).is(":visible"))) {
        information.show();
    }
    else {
        information.hide();
    }    
}
