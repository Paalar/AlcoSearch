$(document).ready(function() {

  $("#infoTable").DataTable( {
    paging: false,
    searching: false,
    info: false,
    "order" : [[2, "asc"]]
  });

  $("#inStore").click(function() {
    var $rowNo = $("#infoTable tbody tr").filter(function() {
      return $.trim($(this).find("td").eq(6).text()) == "Må bestilles"
    }).toggle();
  })

  $("#advancedSearch").hide();

  $("#avsøk").click(function(){
    if($("#advancedSearch").is(":visible")) {
      $("#advancedSearch").hide();
    } else {
      $("#advancedSearch").show();
    }
  })

var vinClicked = false;
  $("#vinAvn").click(function(){
    if($(".vin").is(":checked")) {
      $(".vin").prop("checked", false);
    } else {
      $(".vin").prop("checked", true);
    }
  })

  $("#brennAvn").click(function(){
    if($(".brennevin").is(":checked")) {
      $(".brennevin").prop("checked", false);
    } else {
      $(".brennevin").prop("checked", true);
    }
  })

  $("#chapAvn").click(function(){
    if($(".champagne").is(":checked")) {
      $(".champagne").prop("checked", false);
    } else {
      $(".champagne").prop("checked", true);
    }
  })

  $("#olAvn").click(function(){
    if($(".ol").is(":checked")) {
      $(".ol").prop("checked", false);
    } else {
      $(".ol").prop("checked", true);
    }
  })

  $("#alkfriAvn").click(function(){
    if($(".alkoholfritt").is(":checked")) {
      $(".alkoholfritt").prop("checked", false);
    } else {
      $(".alkoholfritt").prop("checked", true);
    }
  })

});
