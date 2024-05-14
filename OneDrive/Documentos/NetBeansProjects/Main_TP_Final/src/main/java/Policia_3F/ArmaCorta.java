/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Policia_3F;

/**
 *
 * @author eskor
 */
public class ArmaCorta extends Arma {
     private boolean esAutomatica;

    public ArmaCorta(int cantMuniciones, double alcance, String marca, int calibre, String estado, boolean esAutomatica) {
        this.cantMuniciones = cantMuniciones;
        this.alcance = alcance;
        this.marca = marca;
        this.calibre = calibre;
        this.estado = estado;
        this.esAutomatica = esAutomatica;
    }

    @Override
    public boolean enCondicion() {
        return estado.equals("EN USO") && calibre >= 9;
    }

    public boolean efectividadMts() {
        return alcance > 200;
    }
    
}
