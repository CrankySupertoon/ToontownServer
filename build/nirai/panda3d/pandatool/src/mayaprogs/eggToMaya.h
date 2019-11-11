// Filename: eggToMaya.h
// Created by:  drose (11Aug05)
//
////////////////////////////////////////////////////////////////////
//
// PANDA 3D SOFTWARE
// Copyright (c) Carnegie Mellon University.  All rights reserved.
//
// All use of this software is subject to the terms of the revised BSD
// license.  You should have received a copy of this license along
// with this source code in a file named "LICENSE."
//
////////////////////////////////////////////////////////////////////

#ifndef EGGTOMAYA_H
#define EGGTOMAYA_H

#include "pandatoolbase.h"

#include "eggToSomething.h"

////////////////////////////////////////////////////////////////////
//       Class : EggToMaya
// Description : A program to read an egg file and write a maya file.
////////////////////////////////////////////////////////////////////
class EggToMaya : public EggToSomething {
public:
  EggToMaya();

  void run();

private:
  bool _convert_anim;
  bool _convert_model;
  bool _respect_normals;
};

#endif

