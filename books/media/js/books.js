function showInformation(button) {
    var information = $(button).parent().parent().find('.information');
    if (!($(information).is(":visible"))) {
        information.show();
    }
    else {
        information.hide();
    }    
}

function changeList(listSelector) {
    if ($(listSelector).hasClass('selected_list')) {
        return;
    }   
    $(listSelector).parent().find('.list_title').removeClass('selected_list');
    $(listSelector).addClass('selected_list');
    switch(listSelector.id) {
        case 'list1':
            showList('listing1');
            break;
        case 'list2':
            showList('listing2');
            break;
        case 'list3':
            showList('listing3');
            break;
    }
                
} 

function showList(list) {
    $("#list_container").find('.list').hide();
    $("#" + list).show();
}

function showDefaultList() {
    showList('listing1');
}
