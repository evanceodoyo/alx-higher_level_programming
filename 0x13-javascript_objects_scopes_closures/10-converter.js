exports.converter = function (base) {
  return function (k) {
    return k.toString(base);
  };
};
