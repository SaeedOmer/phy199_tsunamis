# used https://github.com/shantnu/PyQt_first/blob/master/pyqt_skeleton.py
# for skeleton code on which paramGenerator.py builds on
# Creates new qt GUI application, initializes parent classes, 
# and loads GUI file into memory

import sys
#from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
#from myapp_auto import Ui_MainWindow
 
qtCreatorFile = "paramGenerator.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
#class MyApp(QtGui.MainWindow, Ui_MainWindow):
#    def __init__(self):
#        QtGui.MainWindow.__init__(self)
#        Ui_MainWindow.__init__(self)
#        self.setupUi(self)
#        self.generateFile.clicked.connect(self.ReadData)

class MyApp(QMainWindow, Ui_MainWindow):
    parse_triggered = pyqtSignal()

    #def __init__(self, parent=None, name=None):
    def __init__(self, parent=None, name=None):
        #super(MyApp, self).__init__(parent)
        super(MyApp, self).__init__()
        self.setupUi(self)
        self.generateFile.clicked.connect(self.ReadData)
        

    def ReadData(self):
        percentNum = str(self.floatprecision_spinBox.value())
        bumpheight = self.bumpheight_box.toPlainText()
        gaussheight = self.gaussheight_box.toPlainText()
        gaussstd = self.gaussstd_box.toPlainText()
        flatdepth = self.flatdepth_box.toPlainText()
        ndiffusions = str(self.ndiffusions_spinBox.value())
        dt = str(self.dt_spinBox.value())
        Nsteps = str(self.Nsteps_spinBox.value())
        numThreads = str(self.numthreads_spinBox.value())

        pfile = open('params.txt', 'w')
        pfile.write("current_step 0\n")
        pfile.write("update_step 1\n")
        pfile.write("save_step 1\n")
        pfile.write("time 0.0\n")
        pfile.write("output_num_digits_for_percent ")
        pfile.write(percentNum)
        pfile.write("\nbump_height ") 
        pfile.write(bumpheight)
        pfile.write("gauss_height ") 
        pfile.write(gaussheight)
        pfile.write("gauss_std ") 
        pfile.write(gaussstd)
        pfile.write("flat_depth ") 
        pfile.write(flatdepth)
        pfile.write("ndiffusions ") 
        pfile.write(ndiffusions)
        pfile.write("\ndt ") 
        pfile.write(dt)
        pfile.write("\nN_steps ") 
        pfile.write(Nsteps)
        pfile.write("\nnum_threads ")
        pfile.write(numThreads)
        pfile.write("\n")
        #pfile.close()
        #self.ReadBools


    #def ReadBools(self):
        #pfile = open('params.txt', 'a')
        pfile.write("move_bool ")
        if self.movebool_yes.isChecked() is True:
            pfile.write("True\n")
        else:
            pfile.write("False\n")
        pfile.write("flatten_bool ")    
        if self.flattenbool_yes.isChecked() is True:
            pfile.write("True\n")
        else:
            pfile.write("False\n")
        pfile.write("diffuse_bool ")
        if self.diffusebool_yes.isChecked() is True:
            pfile.write("True\n")
        else:
            pfile.write("False\n")
        pfile.write("accel_bool ")
        if self.accelbool_yes.isChecked() is True:
            pfile.write("True\n")
        else: 
            pfile.write("False\n")
        pfile.write("check_sim_health ")
        if self.checksimhealth_yes.isChecked() is True:
            pfile.write("True\n")
        else:
            pfile.write("False\n")
        pfile.write("doPlaneFit ")
        if self.doplanefit_yes.isChecked() is True:
            pfile.write("True\n")
        else: 
            pfile.write("False\n")
        pfile.write("write_sim_state ")
        if self.writesimstate_yes.isChecked() is True:
            pfile.write("True\n")
        else: 
            pfile.write("False\n")
        #pfile.close()

    #def ReadStrings(self):


        outfilename = self.outfilename_box.toPlainText()
        bathyfile = self.bathyfile_box.toPlainText()
        initialconditions = self.initialconditions_comboBox.currentText()
        deformationfile = self.deformationfile_box.toPlainText()
        initialstatefilename = self.initialstatefilename_box.toPlainText()
        finalstatefilename = self.finalstatefilename_box.toPlainText()

        pfile.write("out_file_name ")
        pfile.write(outfilename)
        pfile.write("bathy_file ")
        pfile.write(bathyfile)
        pfile.write("initial_conditions ")
        pfile.write(initialconditions)
        pfile.write("\ndeformation_file ")
        pfile.write(deformationfile)
        pfile.write("initialstate_file_name ")
        pfile.write(initialstatefilename)
        pfile.write("finalstate_file_name ")
        pfile.write(finalstatefilename)
        pfile.write(" ")

        pfile.close()
        
#if __name__ == "__main__":
def main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

main()