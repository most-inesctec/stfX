package sftX.Services;

import com.mathworks.engine.MatlabEngine;
import dk.ange.octave.OctaveEngine;
import dk.ange.octave.OctaveEngineFactory;

import java.io.*;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;

public class MPSClientExample {

    public MPSClientExample() throws ExecutionException, InterruptedException {
//        //Start MATLAB asynchronously
//        MatlabEngine ml = MatlabEngine.startMatlab();
//        // Get engine instance
//        //MatlabEngine ml = eng.get();
//        // Calling  a builtin function
//        ml.eval("disp('hello world')");
//        // Evaluate the command to cd to your functio
////        ml.eval("cd '../../../resources/static/PR-GLS-master'");
////        // Evaluate the function
////        ml.eval("test()");
//        //ml.eval("myFunction(args)");


        // Octave attempt
        OctaveEngineFactory factory = new OctaveEngineFactory();
        StringWriter out = new StringWriter();
        StringWriter err = new StringWriter();
        factory.setOctaveInputLog(out);
        factory.setErrorWriter(err);
        factory.setOctaveProgram(new File(this.getClass().getClassLoader().getResource("static/PR-GLS-master/demo.m").getFile()));

        OctaveEngine engine = factory.getScriptEngine();
        engine.eval("demo()");

        System.out.print(out.toString());
        System.err.print(err.toString());
    }
}
