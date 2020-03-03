package sftX.Controllers.MatLabClient;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import sftX.Services.MPSClientExample;

import java.util.concurrent.ExecutionException;

@RestController
public class MatLabController {

    @GetMapping("/matlab-test")
    public void matlabTest() {
        try {
            new MPSClientExample();
        } catch (ExecutionException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
