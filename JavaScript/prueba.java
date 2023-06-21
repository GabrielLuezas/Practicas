import java.util.Random;
import java.util.Scanner;

public class AdivinaElNumero {
    public static void main(String[] args) {
        int numeroAdivinar;
        int intentos = 0;
        boolean acertado = false;
        
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        
        System.out.println("¡Bienvenido a Adivina el Número!");
        System.out.println("Estoy pensando en un número del 1 al 100. ¡Intenta adivinarlo!");

        numeroAdivinar = random.nextInt(100) + 1;

        while (!acertado) {
            System.out.print("Ingresa tu intento: ");
            int intento = scanner.nextInt();
            intentos++;
            
            if (intento == numeroAdivinar) {
                acertado = true;
                System.out.println("¡Felicitaciones! ¡Adivinaste el número en " + intentos + " intentos!");
            } else if (intento < numeroAdivinar) {
                System.out.println("El número es mayor. Sigue intentando.");
            } else {
                System.out.println("El número es menor. Sigue intentando.");
            }
        }
        
        scanner.close();
    }
}