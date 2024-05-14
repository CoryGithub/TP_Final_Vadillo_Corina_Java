/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Policia_3F;

/**
 *
 * @author eskor
 */
public class ArmaLarga extends Arma implements Comparable<ArmaLarga>{
    private String justifUso;
    private int nivelArma;
    private boolean tieneSello;

    public ArmaLarga(int cantMuniciones, double alcance, String marca, int calibre, String estado, String justifUso, int nivelArma, boolean tieneSello) {
        this.cantMuniciones = cantMuniciones;
        this.alcance = alcance;
        this.marca = marca;
        this.calibre = calibre;
        this.estado = estado;
        this.justifUso = justifUso;
        this.nivelArma = nivelArma;
        this.tieneSello = tieneSello;
    }

    @Override
    public boolean enCondicion() {
        return estado.equals("EN USO") && calibre >= 9;
    }

    @Override
    public int compareTo(ArmaLarga otraArma) {
        return Integer.compare(this.nivelArma, otraArma.nivelArma);
    }
      @Override
    public String toString() {
        return "Marca: " + marca + ", Nivel de Arma: " + nivelArma;
    }
    
}
