#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Practitioner) on 2015-07-06.
#  2015, SMART Health IT.


from . import address
from . import attachment
from . import codeableconcept
from . import contactpoint
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import humanname
from . import identifier
from . import period


class Practitioner(domainresource.DomainResource):
    """ A person with a  formal responsibility in the provisioning of healthcare or
    related services.
    
    A person who is directly or indirectly involved in the provisioning of
    healthcare.
    """
    
    resource_name = "Practitioner"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.address = None
        """ Where practitioner can be found/visited.
        List of `Address` items (represented as `dict` in JSON). """
        
        self.birthDate = None
        """ The date  of birth for the practitioner.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.communication = None
        """ A language the practitioner is able to use in patient communication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """
        
        self.identifier = None
        """ A identifier for the person as this agent.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None
        """ A name associated with the person.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.photo = None
        """ Image of the person.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.practitionerRole = None
        """ The list of Roles/Organizations that the Practitioner is associated
        with.
        List of `PractitionerPractitionerRole` items (represented as `dict` in JSON). """
        
        self.qualification = None
        """ Qualifications obtained by training and certification.
        List of `PractitionerQualification` items (represented as `dict` in JSON). """
        
        self.telecom = None
        """ A contact detail for the practitioner.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(Practitioner, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Practitioner, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, True),
            ("birthDate", "birthDate", fhirdate.FHIRDate, False),
            ("communication", "communication", codeableconcept.CodeableConcept, True),
            ("gender", "gender", str, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("name", "name", humanname.HumanName, False),
            ("photo", "photo", attachment.Attachment, True),
            ("practitionerRole", "practitionerRole", PractitionerPractitionerRole, True),
            ("qualification", "qualification", PractitionerQualification, True),
            ("telecom", "telecom", contactpoint.ContactPoint, True),
        ])
        return js


class PractitionerPractitionerRole(fhirelement.FHIRElement):
    """ The list of Roles/Organizations that the Practitioner is associated with.
    """
    
    resource_name = "PractitionerPractitionerRole"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.healthcareService = None
        """ The list of healthcare services that this worker provides for this
        role's Organization/Location(s).
        List of `FHIRReference` items referencing `HealthcareService` (represented as `dict` in JSON). """
        
        self.location = None
        """ The location(s) at which this practitioner provides care.
        List of `FHIRReference` items referencing `Location` (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        """ The Organization where the Practitioner performs the roles
        associated.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.period = None
        """ The period during which the practitioner is authorized to perform
        in these role(s).
        Type `Period` (represented as `dict` in JSON). """
        
        self.role = None
        """ Roles which this practitioner may perform.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.specialty = None
        """ Specific specialty of the practitioner.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(PractitionerPractitionerRole, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(PractitionerPractitionerRole, self).elementProperties()
        js.extend([
            ("healthcareService", "healthcareService", fhirreference.FHIRReference, True),
            ("location", "location", fhirreference.FHIRReference, True),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False),
            ("period", "period", period.Period, False),
            ("role", "role", codeableconcept.CodeableConcept, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True),
        ])
        return js


class PractitionerQualification(fhirelement.FHIRElement):
    """ Qualifications obtained by training and certification.
    """
    
    resource_name = "PractitionerQualification"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Coded representation of the qualification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ An identifier for this qualification for the practitioner.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.issuer = None
        """ Organization that regulates and issues the qualification.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.period = None
        """ Period during which the qualification is valid.
        Type `Period` (represented as `dict` in JSON). """
        
        super(PractitionerQualification, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(PractitionerQualification, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("issuer", "issuer", fhirreference.FHIRReference, False),
            ("period", "period", period.Period, False),
        ])
        return js

