$(document).ready(function(){
    $('#contactcard').html(localStorage.getItem("data"));
  
  $(document).on("click",".btn",function(){
    var id=$('#first').val()+$('#last').val()
    var str = '<div class = "contactcard" id='+id+'><h1>'+$('#first').val()+" "+$('#last').val()+'</h1>\<h2>'+$('#description').val()+'</h2>\<h3>click for description</h3></div>'
    $('#directory').append(str);
    localStorage.setItem("data", $('#directory').html());

      $("h2").hide();
      
      $("#"+id).on("click",function(){
      $("#"+id+" h2").toggle("slow",function(){});
      $("#"+id+" h1").toggle("slow",function(){});
      $("#"+id+" h3").toggle("slow",function(){});

      
    });
    
  });
  });