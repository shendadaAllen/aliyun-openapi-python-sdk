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
class VerifyPhoneRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Green', '2017-08-23', 'VerifyPhone','green')

	def get_VerifyCode(self):
		return self.get_query_params().get('VerifyCode')

	def set_VerifyCode(self,VerifyCode):
		self.add_query_param('VerifyCode',VerifyCode)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_Phone(self):
		return self.get_query_params().get('Phone')

	def set_Phone(self,Phone):
		self.add_query_param('Phone',Phone)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)