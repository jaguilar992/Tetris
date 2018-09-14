var FORMS = {
  'cuadro': 0,
  'linea': 1,
  'te': 2,
  'gancho_izq': 3,
  'silla_izq': 4,
  'gancho_der': 5,
  'silla_der': 6,
};

var DEFN = [
  [[0,0],[0,1],[-1,0],[-1,1]],
  [[0,0],[-1,0],[-2,0],[-3,0]],
  [[0,0],[0,1],[0,2],[-1,3]],
  [[0,0],[0,1],[0,2],[-1,0]],
  [[0,0],[0,1],[-1,1],[-1,2]],
  [[0,0],[0,1],[0,2],[-1,2]],
  [[0,1],[0,2],[-1,0],[-1,1]]
];

class forma{
  constructor(fil, col){
    this.fil=fil;
    this.col=col;
    this.forma= 0;
    this.rotacion = 0;
  }

  setForma(nombre){
    if (nombre in FORMS) {
      this.forma = FORMS[nombre];
    }
  }

  setRotacion(n){
    if (n>=0 && n<=3){
      this.rotacion = n;
    }
  }

  print(){
    for (var pixel of DEFN[this.forma]){
      on(this.fil + pixel[0], this.col+ pixel[1]);
    }
  }
}

var l = new forma(-1,10);
l.setForma('te');
l.print();

setInterval(function(){
  cls();
  l.fil=l.fil+1
  l.print()
}, 1000);