$(document).ready(function(){
    $('#list').html(localStorage.getItem("data"));
    
  });
  function addRow(){
    var str = '<tr class = "boxType"><td>'+$('#firstname').val()+'</td>\
<td>'+$('#lastname').val()+'</td>\
<td>'+$('#email').val()+'</td>\
<td>'+$('#contactnum').val()+'</td>\
</tr>'
    $('#list').append(str);
    localStorage.setItem("data", $('#list').html());
  }