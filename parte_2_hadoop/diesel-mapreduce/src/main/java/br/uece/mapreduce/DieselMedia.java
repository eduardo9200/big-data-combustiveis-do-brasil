package br.uece.mapreduce;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class DieselMedia {

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Media do Preco do Diesel no estado de SP");

        job.setJarByClass(DieselMedia.class);
        job.setMapperClass(DieselMapper.class);
        job.setReducerClass(DieselReducer.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(FloatWritable.class);

        FileInputFormat.addInputPath(job, new Path("/user/root/input"));
        FileOutputFormat.setOutputPath(job, new Path("/user/root/output"));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
