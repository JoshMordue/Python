from PrescriptionData import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# remove warfarin and add edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        print(f"Patient {patient} is not taking warfarin."
              f"Please remove {patient} from the trial")
    print(patient, prescription)
