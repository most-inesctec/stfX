package sftX.Services;

import com.mathworks.engine.MatlabEngine;

import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;

public class MPSClientExample {

    public MPSClientExample() throws ExecutionException, InterruptedException {
        //Start MATLAB asynchronously
        MatlabEngine ml = MatlabEngine.startMatlab();
        // Get engine instance
        //MatlabEngine ml = eng.get();
        // Calling  a builtin function
        ml.eval("disp('hello world')");
        // Evaluate the command to cd to your functio
//        ml.eval("cd '../../../resources/static/PR-GLS-master'");
//        // Evaluate the function
//        ml.eval("test()");
        //ml.eval("myFunction(args)");
    }
}
