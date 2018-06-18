#include "Exception.js"
#include "Ship.js"
#include "BattleField.js"


/**
  * class FieldNotFoundException
  * docstring for EieldNotFoundException.
  */

FieldNotFoundException = function ()
{
  this._init ();
}

FieldNotFoundException.prototype = new Exception ();

/**
 * _init sets all FieldNotFoundException attributes to their default value. Make
 * sure to call this method within your class constructor
 */
FieldNotFoundException.prototype._init = function ()
{

  /**Aggregations: */

  /**Compositions: */

}

/**
 * 
 */
FieldNotFoundException.prototype.__init__ = function ()
{
  super(FieldNotFoundException,self).__init__()
  
}



