public class Main {

    public static void main(String[] args) {
        int[][] prueba = {
                {1, 1, 1, 1,0,0,1,1},
                {1, 0, 0, 1,0,0,0,1},
                {0, 1, 1, 0,1,0,8,1},
                {0, 1, 1, 0,8,0,1,1},
                {0, 1, 0, 1,1,1,0,0},
                {1, 1, 1, 1,0,0,1,1},
                {1, 1, 1, 1,0,0,1,1},
                {0, 1, 0, 1,1,1,0,0}
        };
        // matriz inicial
        imprimir(prueba);

        // cambiar
        desplazar(prueba);

        // nueva matriz
        imprimir(prueba);
    }

    static void desplazar(int[][] matriz) {
        System.out.println("Desplazando...");
        for (int i = matriz.length - 1; i >= 0; i--) {
            for (int j = 0; j < matriz[0].length; j++) {
                if (i == 0) {
                    // llegamos a la primera linea, entonces la borramos
                    matriz[i][j] = 0;
                } else {
                    // tomamos el valor de la linea superior
                    matriz[i][j] = matriz[i - 1][j];
                }
            }
        }
    }

    static void imprimir(int[][] matriz) {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[0].length; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }
}
