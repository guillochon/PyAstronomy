from numpy import pi, sqrt, exp, meshgrid
from onedfit import OneDFit
from PyAstronomy.pyaC import pyaErrors as PE

class GaussFit2d(OneDFit):
  """
    Implements a two dimensional Gaussian.
    
    Expects a coordinate array to evaluate model.
    
    The functional form is:
  
    .. math:: \\frac{A}{2\\pi\\sigma_x\\sigma_y\\sqrt{1-\\rho^2}}
              exp\\left(-\\frac{1}{2(1-\\rho^2)}\left( \\frac{(x-\\mu_x)^2}{\\sigma_x^2} +
              \\frac{(y-\\mu_y)^2}{\\sigma_y^2} -
              \\frac{2\\rho(x-\\mu_x)(y-\\mu_y)}{\\sigma_x\\sigma_y}
              \\right)\\right)
    
    Here, `lin` and `off` denote the linear and the offset term.
    
    *Fit parameters*:
     - `A` - Amplitude (the area of the Gaussian)
     - `mux` - Center of the Gaussian (x-axis)
     - `muy` - Center of the Gaussian (y-axis)
     - `sigx` - Standard deviation (x-axis)
     - `sigy` - Standard deviation (y-axis)
     - `rho` - Correlation
  """
  
  def __init__(self):
    OneDFit.__init__(self, ["A", "mux", "muy", "sigx", "sigy", "rho"])
    self.setRootName("Gaussian2d")

  def evaluate(self, co):
    """
      Evaluates the model for current parameter values.
      
      Parameters
      ----------
      co : array
           Specifies the points at which to evaluate the model.
    """
    if (self["sigx"] <= 0.0) or (self["sigy"] <= 0.0):
      raise(PE.PyAValError("Width(s) of Gaussian must be larger than zero.", \
                           solution="Change width ('sigx/y')."))
    if self["rho"] > 1.0:
      raise(PE.PyAValError("The correlation coefficient must be 0 <= rho <= 1.", \
                           solution="Change width ('sigx/y')."))
    result = self["A"]/(2.*pi*self["sigx"]*self["sigy"]*sqrt(1.-self["rho"]**2)) * \
        exp( ((co[::,::,0]-self["mux"])**2/self["sigx"]**2 + (co[::,::,1]-self["muy"])**2/self["sigy"]**2 - \
            2.*self["rho"]*(co[::,::,0]-self["mux"])*(co[::,::,1]-self["muy"])/(self["sigx"]*self["sigy"])) / \
            (-2.*(1.-self["rho"]**2)) )
    return result



class GaussFit2dTuple(OneDFit):
  """
    Implements a two dimensional Gaussian.
    
    Expects a tuple or list of coordinate axes to evaluate the model.
    
    The functional form is:
  
    .. math:: \\frac{A}{2\\pi\\sigma_x\\sigma_y\\sqrt{1-\\rho^2}}
              exp\\left(-\\frac{1}{2(1-\\rho^2)}\left( \\frac{(x-\\mu_x)^2}{\\sigma_x^2} +
              \\frac{(y-\\mu_y)^2}{\\sigma_y^2} -
              \\frac{2\\rho(x-\\mu_x)(y-\\mu_y)}{\\sigma_x\\sigma_y}
              \\right)\\right)
    
    Here, `lin` and `off` denote the linear and the offset term.
    
    *Fit parameters*:
     - `A` - Amplitude (the area of the Gaussian)
     - `mux` - Center of the Gaussian (x-axis)
     - `muy` - Center of the Gaussian (y-axis)
     - `sigx` - Standard deviation (x-axis)
     - `sigy` - Standard deviation (y-axis)
     - `rho` - Correlation
  """
  
  def __init__(self):
    OneDFit.__init__(self, ["A", "mux", "muy", "sigx", "sigy", "rho"])
    self.setRootName("Gaussian2d")

  def evaluate(self, co):
    """
      Evaluates the model for current parameter values.
      
      Parameters
      ----------
      co : array
           Specifies the points at which to evaluate the model.
    """
    if (self["sigx"] <= 0.0) or (self["sigy"] <= 0.0):
      raise(PE.PyAValError("Width(s) of Gaussian must be larger than zero.", \
                           solution="Change width ('sigx/y')."))
    if self["rho"] > 1.0:
      raise(PE.PyAValError("The correlation coefficient must be 0 <= rho <= 1.", \
                           solution="Change width ('sigx/y')."))
    xx, yy = meshgrid(co[0], co[1])
    result = self["A"]/(2.*pi*self["sigx"]*self["sigy"]*sqrt(1.-self["rho"]**2)) * \
        exp( ((xx-self["mux"])**2/self["sigx"]**2 + (yy-self["muy"])**2/self["sigy"]**2 - \
            2.*self["rho"]*(xx-self["mux"])*(yy-self["muy"])/(self["sigx"]*self["sigy"])) / \
            (-2.*(1.-self["rho"]**2)) )
    return result