from django.dispatch import Signal


connection_request_created = Signal()
connection_request_rejected = Signal()
connection_request_canceled = Signal()
connection_request_viewed = Signal()
connection_request_accepted = Signal()
connection_removed = Signal()
