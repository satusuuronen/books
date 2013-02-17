function showInformation(list_button) {
    var information = $(list_button).parent().parent().find('.information');
    if (!($(information).is(":visible"))) {
        information.show();
        $(list_button).html("-");
        $(list_button).show();
        $(list_button).removeClass('no_show');
        $(list_button).addClass('shown');
    }
    else {
        information.hide();
        $(list_button).html("+");
        $(list_button).show();
        $(list_button).removeClass('shown');
        $(list_button).addClass('no_show');
    }    
}

function showAll() {
    $("#list_container").find('.list_button.no_show').click();
}

function hideAll(){
    $("#list_container").find('.list_button.shown').click();
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
        case 'list4':
            showList('listing4');
            break;
    }
    hideAll();
} 

function showList(list) {
    $("#list_container").find('.list').hide();
    $("#" + list).show();
}

function showDefaultList() {
    var list = getUrlParameter('list');
    if (list === undefined) {
        showList('listing1');
    }
    else {
        showList('listing' + list);
    $("#title_menu").find('.list_title').removeClass('selected_list');
    $("#list" + list).addClass('selected_list');
    }
}

function sortList(sortBy) {
    var sorter = $(sortBy).attr("value");
    var url = document.location.toString().split("?")[0];
    url += "?sort=" + sorter;
    var selectedList = $("#title_menu").find('.selected_list').attr('id');
    selectedList = selectedList[selectedList.length - 1];
    url += "&list=" + selectedList;
    document.location = url;
}

function setupComponents() {
    var sorter = getUrlParameter("sort");
    if (sorter === undefined) {
        sorter = $("#list_container").find('.sorted_by').attr("value");
    }
    var selectedOption = $("#list_container").find('.sort_option[value='+ sorter +']')
    selectedOption.hide();
    $("#list_container").find('.sorted_by').html(selectedOption.html());
    $("#list_container").find('.sorted_by').attr("value", sorter);
            
}

function getUrlParameter(name) {
    var urlParameters = document.location.toString().split("?")[1];
    if (urlParameters === undefined) {
        return
    }
    urlParameters = urlParameters.split("&");
    for (index in urlParameters) {
        var parameter = urlParameters[index].split("=");
        if (parameter[0] === name) {
            return parameter[1];
        }
    }
}
