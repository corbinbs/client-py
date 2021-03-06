#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/ReferralRequest) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period


class ReferralRequest(domainresource.DomainResource):
    """ A request for referral or transfer of care.
    
    Used to record and send details about a request for referral service or
    transfer of a patient to the care of another provider or provider
    organisation.
    """
    
    resource_name = "ReferralRequest"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.dateSent = None
        """ Date referral/transfer of care request is sent.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ A textual description of the referral.
        Type `str`. """
        
        self.encounter = None
        """ Encounter.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.fulfillmentTime = None
        """ Requested service(s) fulfillment time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifier of request.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Patient referred to care or transfer.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.priority = None
        """ Urgency of referral / transfer of care request.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Reason for referral / Transfer of care request.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.recipient = None
        """ Receiver of referral / transfer of care request.
        List of `FHIRReference` items referencing `Practitioner, Organization` (represented as `dict` in JSON). """
        
        self.requester = None
        """ Requester of referral / transfer of care.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient` (represented as `dict` in JSON). """
        
        self.serviceRequested = None
        """ Service(s) requested.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialty = None
        """ The clinical specialty (discipline) that the referral is requested
        for.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | requested | active | cancelled | accepted | rejected |
        completed.
        Type `str`. """
        
        self.supportingInformation = None
        """ Additonal information to support referral or transfer of care
        request.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.type = None
        """ Referral/Transition of care request type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ReferralRequest, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ReferralRequest, self).elementProperties()
        js.extend([
            ("dateSent", "dateSent", fhirdate.FHIRDate, False),
            ("description", "description", str, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("fulfillmentTime", "fulfillmentTime", period.Period, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False),
            ("reason", "reason", codeableconcept.CodeableConcept, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True),
            ("requester", "requester", fhirreference.FHIRReference, False),
            ("serviceRequested", "serviceRequested", codeableconcept.CodeableConcept, True),
            ("specialty", "specialty", codeableconcept.CodeableConcept, False),
            ("status", "status", str, False),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True),
            ("type", "type", codeableconcept.CodeableConcept, False),
        ])
        return js

