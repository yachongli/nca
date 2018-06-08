# Copyright (c) 2015 Mirantis, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from nca.pecan_wsgi.hooks import body_validation
from nca.pecan_wsgi.hooks import context
from nca.pecan_wsgi.hooks import notifier
from nca.pecan_wsgi.hooks import ownership_validation
from nca.pecan_wsgi.hooks import policy_enforcement
from nca.pecan_wsgi.hooks import query_parameters
from nca.pecan_wsgi.hooks import quota_enforcement
from nca.pecan_wsgi.hooks import translation


ExceptionTranslationHook = translation.ExceptionTranslationHook
ContextHook = context.ContextHook
BodyValidationHook = body_validation.BodyValidationHook
OwnershipValidationHook = ownership_validation.OwnershipValidationHook
PolicyHook = policy_enforcement.PolicyHook
QuotaEnforcementHook = quota_enforcement.QuotaEnforcementHook
NotifierHook = notifier.NotifierHook
QueryParametersHook = query_parameters.QueryParametersHook
