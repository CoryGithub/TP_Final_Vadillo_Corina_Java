/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.main_tp_final;

import Policia_3F.ArmaCorta;
import Policia_3F.ArmaLarga;
import Policia_3F.Policia;

/**
 *
 * @author eskor
 */
public class Main_TP_Final {

    public static void main(String[] args) {
       
       
        Policia policia = new Policia("Juan", "Perez", 1234);
        
        ArmaCorta armaCorta = new ArmaCorta(10, 150.0, "Glock", 9, "EN USO", true);
        ArmaLarga armaLarga1 = new ArmaLarga(20, 500.0, "Remington", 12, "EN USO", "Caza", 3, true);
        ArmaLarga armaLarga2 = new ArmaLarga(15, 800.0, "Winchester", 7, "EN USO", "Caza", 4, true);

        System.out.println("Policía: " + policia);
        System.out.println("Arma corta en condiciones: " + armaCorta.enCondicion());
        System.out.println("Arma corta efectiva a más de 200m: " + armaCorta.efectividadMts());
        System.out.println("Arma larga 1 en condiciones: " + armaLarga1.enCondicion());
        System.out.println("Arma larga 2 en condiciones: " + armaLarga2.enCondicion());
        System.out.println("Arma larga 1 es mayor que arma larga 2: " + (armaLarga1.compareTo(armaLarga2) > 0));
      }
    }

