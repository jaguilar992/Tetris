function cls() {
  $(".cell").removeClass('on');
}

function on (fila, col){
  if (fila>=0 && fila<=23){
    if (col>=0 && col<=15){
      var cell = 16 * fila + col;
      $("#c"+cell).addClass('on');
    }
  }
}

function off (fila, col){
  if (fila>=0 && fila<=23){
    if (col>=0 && col<=15){
      var cell = 16 * fila + col;
      $("#c"+cell).removeClass('on');
    }
  }
}

$('.cell').click(function(){
  $(this).addClass('on');
});