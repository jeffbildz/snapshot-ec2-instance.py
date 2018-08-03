#!/usr/bin/python

import os
import sys
import time
import argparse
import boto3


#if os.environ.get('AWS_PROFILE') is None:
#    sys.exit('Environment variable AWS_PROFILE not set')

argparser = argparse.ArgumentParser(description='Snapshot EC2 instance volume with volume ID specified by argument')
argparser.add_argument('volume_id', help='Volume ID')
argparser.add_argument('--name', help='Snapshot name')
argparser.add_argument('--description', default='Created by backup script', help='Snapshot description')
argparser.add_argument('--verbose', action='store_true', help='Output AWS operations')
args = argparser.parse_args()


snapshot_name = args.name
if args.name is None:
   print "error"

else:

  if args.verbose:
      print "creating snapshot of Volume ID: {0}  Name: {1}       Description: {2}".format(args.volume_id,snapshot_name,args.description)

  ec2 = boto3.resource('ec2')

  snapshot = ec2.create_snapshot(VolumeId=args.volume_id, Description=args.description)
  snapshot.create_tags(Resources=[snapshot.id], Tags=[{'Key': 'Name', 'Value': snapshot_name}])
  if args.verbose:
      print "Creating snapshot ID: {0}".format(snapshot.id)
