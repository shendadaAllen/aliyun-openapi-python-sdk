# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkccc.endpoint import endpoint_data

class ListCallDetailRecordsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2017-07-05', 'ListCallDetailRecords')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ContactType(self):
		return self.get_query_params().get('ContactType')

	def set_ContactType(self,ContactType):
		self.add_query_param('ContactType',ContactType)

	def get_ContactId(self):
		return self.get_query_params().get('ContactId')

	def set_ContactId(self,ContactId):
		self.add_query_param('ContactId',ContactId)

	def get_Criteria(self):
		return self.get_query_params().get('Criteria')

	def set_Criteria(self,Criteria):
		self.add_query_param('Criteria',Criteria)

	def get_PhoneNumber(self):
		return self.get_query_params().get('PhoneNumber')

	def set_PhoneNumber(self,PhoneNumber):
		self.add_query_param('PhoneNumber',PhoneNumber)

	def get_OrderBy(self):
		return self.get_query_params().get('OrderBy')

	def set_OrderBy(self,OrderBy):
		self.add_query_param('OrderBy',OrderBy)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_StopTime(self):
		return self.get_query_params().get('StopTime')

	def set_StopTime(self,StopTime):
		self.add_query_param('StopTime',StopTime)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_ContactDisposition(self):
		return self.get_query_params().get('ContactDisposition')

	def set_ContactDisposition(self,ContactDisposition):
		self.add_query_param('ContactDisposition',ContactDisposition)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_WithRecording(self):
		return self.get_query_params().get('WithRecording')

	def set_WithRecording(self,WithRecording):
		self.add_query_param('WithRecording',WithRecording)