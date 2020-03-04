import subprocess
import oct2py


def benchop():
    oc = oct2py.Oct2Py()
    oc.eval("cd ./PR-GLS-master/CPD")
    oc.eval('mex cpd_P.c')
    oc.eval('mex cpd_Pappmex.c')
    oc.eval('mex cpd_Pcorrespondence.c;')
    oc.eval('cd ..')
    res = oc.feval('prlgdemo')
    #print(res)
    return res

if __name__ == '__main__':
    benchop()