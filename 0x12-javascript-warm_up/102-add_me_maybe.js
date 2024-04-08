#!/usr/bin/node
module.exports.addMeMaybe = (number, theFunction) => {
  number++;
  theFunction(number);
};
