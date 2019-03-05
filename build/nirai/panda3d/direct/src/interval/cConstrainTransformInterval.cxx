// Filename: cConstrainTransformInterval.cxx
// Created by:  pratt (29Sep06)
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

#include "cConstrainTransformInterval.h"
#include "transformState.h"
#include "config_interval.h"

TypeHandle CConstrainTransformInterval::_type_handle;

////////////////////////////////////////////////////////////////////
//     Function: CConstrainTransformInterval::Constructor
//       Access: Published
//  Description: Constructs a constraint interval that will constrain
//               the transform of one node to the transform of another.
//               To clarify, the transform of node will be copied to target.
//
//               If wrt is true, the node's transform will be
//               transformed into the target node's parent's  space
//               before being copied.  If wrt is false, the node's
//               local transform will be copied unaltered.
////////////////////////////////////////////////////////////////////
CConstrainTransformInterval::
CConstrainTransformInterval(const string &name, double duration,
                            const NodePath &node, const NodePath &target,
                            bool wrt) :
  CConstraintInterval(name, duration),
  _node(node),
  _target(target),
  _wrt(wrt)
{
}

////////////////////////////////////////////////////////////////////
//     Function: CConstrainTransformInterval::step
//       Access: Published, Virtual
//  Description: Advances the time on the interval.  The time may
//               either increase (the normal case) or decrease
//               (e.g. if the interval is being played by a slider).
////////////////////////////////////////////////////////////////////
void CConstrainTransformInterval::
priv_step(double t) {
  check_started(get_class_type(), "priv_step");
  _state = S_started;
  _curr_t = t;

  if(! _target.is_empty()) {
    CPT(TransformState) transform;
    if(_wrt) {
      if(! _node.is_same_graph(_target)){
        interval_cat.warning()
          << "Unable to copy transform in CConstrainTransformInterval::priv_step;\n"
          << "node (" << _node.get_name()
          << ") and target (" << _target.get_name()
          << ") are not in the same graph.\n";
        return;
      }
      transform = _node.get_transform(_target.get_parent());
    } else {
      transform = _node.get_transform();
    }

    _target.set_transform(transform);
  }
}

////////////////////////////////////////////////////////////////////
//     Function: CConstrainTransformInterval::output
//       Access: Published, Virtual
//  Description: 
////////////////////////////////////////////////////////////////////
void CConstrainTransformInterval::
output(ostream &out) const {
  out << get_name() << ":";
  out << " dur " << get_duration();
}
