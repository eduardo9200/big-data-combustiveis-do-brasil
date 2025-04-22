package br.uece.mapreduce;

import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

public class DieselMapper extends Mapper<LongWritable, Text, Text, FloatWritable> {

    private static final Text stateKey = new Text("SP");

    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();

        // Ignora o cabeçalho
        if (line.contains("Municipio") || line.contains("Estado - Sigla")) return;

        String[] fields = line.split(";");

        try {
            String estado = fields[1].trim(); // Coluna "Estado"
            String combustivel = fields[10].trim(); // Coluna "Combustível"
            float preco = Float.parseFloat(fields[12].replace(",", ".")); // Coluna "Valor de Venda"

            if (estado.equalsIgnoreCase("SP") && combustivel.contains("DIESEL")) {
                context.write(stateKey, new FloatWritable(preco));
            }

        } catch (Exception e) {
        	System.err.println("Erro: " + e);
        }
    }
}
