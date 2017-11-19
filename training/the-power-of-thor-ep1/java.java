import java.util.*;
import java.io.*;
import java.math.*;

class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int lightX = in.nextInt(); // the X position of the light of power
        int lightY = in.nextInt(); // the Y position of the light of power
        int initialTX = in.nextInt(); // Thor's starting X position
        int initialTY = in.nextInt(); // Thor's starting Y position
        int thorX = initialTX;
        int thorY = initialTY;
        String directionX = new String();
        String directionY = new String();

        // game loop
        while (true) {
            directionX = "";
            directionY = "";
            if (thorX > lightX)
            {
                directionX = "W";
                thorX -= 1;
            }
            else if (thorX < lightX)
            {
                directionX = "E";
                thorX += 1;
            }
            if (thorY > lightY)
            {
                directionY = "N";
                thorY -= 1;
            }
            else if (thorY < lightY)
            {
                directionY = "S";
                thorY += 1;
            }
            System.out.println(directionY + directionX);
        }
    }
}
