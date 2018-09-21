#!/usr/bin/env python
import sys
import os
import boto3
import argparse
import time
import urllib2


def detach(client=None):
    """Detach EBS volume to an Instance."""
    c = client or boto3.client('ec2', 'eu-central-1')
    try:
        c.detach_volume(VolumeId='vol-03dbf76f2743932f9')
    except Exception, e:
        print(e)
        sys.exit(3)

def main():
    client = boto3.client('ec2', 'eu-central-1')
    volume_id = None

    detach()
    sys.exit(0)


if __name__ == "__main__":
    main()

