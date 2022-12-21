$("div.user-content").each(function(){
    $(this).hide();
  if($(this).attr('id') == 'main') {
       $(this).show();
  }
});


$('.user-id').on( "click", function(e) {
   e.preventDefault();
   var id = $(this).attr('data-related'); 
   $("div.user-content").each(function(){
       $(this).hide();
       if($(this).attr('id') == id) {
           $(this).show();
           
       }
   });
});

$(document).ready(function () {

   $('.btn-filter').on('click', function () {
     var $target = $(this).data('target');
     if ($target != 'all') {
       $('tbody tr').css('display', 'none');
       $('tbody tr[data-status="' + $target + '"]').fadeIn('slow');
     } else {
       $('tbody tr').css('display', 'none').fadeIn('slow');
     }
   });



});


// pagination

$.fn.pageMe = function(opts){
   var $this = this,
       defaults = {
           perPage: 7,
           showPrevNext: false,
           hidePageNumbers: false
       },
       settings = $.extend(defaults, opts);
   
   var listElement = $this;
   var perPage = settings.perPage; 
   var children = listElement.children();
   var pager = $('.pager');
   
   if (typeof settings.childSelector!="undefined") {
       children = listElement.find(settings.childSelector);
   }
   
   if (typeof settings.pagerSelector!="undefined") {
       pager = $(settings.pagerSelector);
   }
   
   var numItems = children.size();
   var numPages = Math.ceil(numItems/perPage);

   pager.data("curr",0);
   
   if (settings.showPrevNext){
       $('<li><a href="#" class="prev_link">«</a></li>').appendTo(pager);
   }
   
   var curr = 0;
   while(numPages > curr && (settings.hidePageNumbers==false)){
       $('<li><a href="#" class="page_link">'+(curr+1)+'</a></li>').appendTo(pager);
       curr++;
   }
   
   if (settings.showPrevNext){
       $('<li><a href="#" class="next_link">»</a></li>').appendTo(pager);
   }
   
   pager.find('.page_link:first').addClass('active');
   pager.find('.prev_link').hide();
   if (numPages<=1) {
       pager.find('.next_link').hide();
   }
     pager.children().eq(1).addClass("active");
   
   children.hide();
   children.slice(0, perPage).show();
   
   pager.find('li .page_link').click(function(){
       var clickedPage = $(this).html().valueOf()-1;
       goTo(clickedPage,perPage);
       return false;
   });
   pager.find('li .prev_link').click(function(){
       previous();
       return false;
   });
   pager.find('li .next_link').click(function(){
       next();
       return false;
   });
   
   function previous(){
       var goToPage = parseInt(pager.data("curr")) - 1;
       goTo(goToPage);
   }
    
   function next(){
       goToPage = parseInt(pager.data("curr")) + 1;
       goTo(goToPage);
   }
   
   function goTo(page){
       var startAt = page * perPage,
           endOn = startAt + perPage;
       
       children.css('display','none').slice(startAt, endOn).show();
       
       if (page>=1) {
           pager.find('.prev_link').show();
       }
       else {
           pager.find('.prev_link').hide();
       }
       
       if (page<(numPages-1)) {
           pager.find('.next_link').show();
       }
       else {
           pager.find('.next_link').hide();
       }
       
       pager.data("curr",page);
         pager.children().removeClass("active");
       pager.children().eq(page+1).addClass("active");
   
   }
};

$(document).ready(function(){
   
 $('#user').pageMe({pagerSelector:'#myPager',showPrevNext:true,hidePageNumbers:false,perPage:3});
   
});


//search filter

/*
Please consider that the JS part isn't production ready at all, I just code it to show the concept of merging filters and titles together !
*/
$(document).ready(function(){
   $('.filterable .btn-filter1').click(function(){
       var $panel = $(this).parents('.filterable'),
       $filters = $panel.find('.filters input'),
       $tbody = $panel.find('.table tbody');
       if ($filters.prop('disabled') == true) {
           $filters.prop('disabled', false);
           $filters.first().focus();
       } else {
           $filters.val('').prop('disabled', true);
           $tbody.find('.no-result').remove();
           $tbody.find('tr').show();
       }
   });

   $('.filterable .filters input').keyup(function(e){
       /* Ignore tab key */
       var code = e.keyCode || e.which;
       if (code == '9') return;
       /* Useful DOM data and selectors */
       var $input = $(this),
       inputContent = $input.val().toLowerCase(),
       $panel = $input.parents('.filterable'),
       column = $panel.find('.filters th').index($input.parents('th')),
       $table = $panel.find('.table'),
       $rows = $table.find('tbody tr');
       /* Dirtiest filter function ever ;) */
       var $filteredRows = $rows.filter(function(){
           var value = $(this).find('td').eq(column).text().toLowerCase();
           return value.indexOf(inputContent) === -1;
       });
       /* Clean previous no-result if exist */
       $table.find('tbody .no-result').remove();
       /* Show all rows, hide filtered ones (never do that outside of a demo ! xD) */
       $rows.show();
       $filteredRows.hide();
       /* Prepend no-result row if all rows are filtered */
       if ($filteredRows.length === $rows.length) {
           $table.find('tbody').prepend($('<tr class="no-result text-center"><td colspan="'+ $table.find('.filters th').length +'">No result found</td></tr>'));
       }
   });
});