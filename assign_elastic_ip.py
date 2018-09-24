#!/usr/bin/python
import boto
from boto.utils import get_instance_metadata

instance_id = get_instance_metadata()['instance-id']

ec2Client.associate_address(
     DryRun = False,
     InstanceId = instance_id,
     AllocationId = "eipalloc-067272a34a220d1dc")
     
