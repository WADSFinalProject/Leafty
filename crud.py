from sqlalchemy.orm import Session
import models
import schemas
import uuid

#sessions
def create_session(db: Session, session_id:str, user_id: str):
    db_session = models.SessionData(session_id=session_id, user_id = user_id)
    db.add(db_session)
    db.commit()

def check_session(db: Session, session_id: str):
    db_session = db.query(models.SessionData).filter(session_id = session_id)
    return db_session

def delete_session(db: Session):
    db.query(models.SessionData).delete()
    db.commit()

#users
def create_user(db: Session, user: schemas.UserCreate):
  
    user_uuid = str(uuid.uuid4())
   
    db_user = models.User(**user.dict(), UserID=user_uuid)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_role(db: Session, RoleID: int):
    return db.query(models.User).filter(models.User.RoleID == RoleID).all()

def get_users(db: Session, limit: int = 100):
    return db.query(models.User).limit(limit).all()

def get_user_by_id(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.UserID == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.Email == email).first()

def update_user(db: Session, user_id: uuid.UUID, user_update: schemas.UserUpdate):
    user = db.query(models.User).filter(models.User.UserID == user_id).first()
    if not user:
        return None
    user.Username = user_update.Username
    user.Email = user_update.Email
    user.Password = user_update.Password 
    db.commit()
    db.refresh(user)
    return user

def update_user_role(db: Session, user_id: str, role_id: int):
    user = db.query(models.User).filter(models.User.UserID == user_id).first()
    if not user:
        return None
    user.RoleID = role_id
    db.commit()
    db.refresh(user)
    return user

def delete_user_by_id(db: Session, user_id: str):
    db_user = db.query(models.User).filter(models.User.UserID == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False

# roles
def create_role(db: Session, role: schemas.RoleCreate):
    db_role = models.RoleModel(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_role(db: Session, role_id: int):
    return db.query(models.RoleModel).filter(models.RoleModel.RoleID == role_id).first()

def get_roles(db: Session):
    return db.query(models.RoleModel).all()

def delete_role_by_id(db: Session, role_id: str):
    db_user = db.query(models.RoleModel).filter(models.RoleModel.RoleID == role_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False

#courier
def create_courier(db: Session, courier: schemas.CourierCreate):
    db_courier = models.Courier(**courier.dict())
    db.add(db_courier)
    db.commit()
    db.refresh(db_courier)
    return db_courier

def get_couriers(db: Session):
    return db.query(models.Courier).all()

def delete_courier(db: Session, courier_id: int):
    courier_delete = db.query(models.Courier).filter(models.Courier.CourierID == courier_id).first()
    if courier_delete:
        db.delete(courier_delete)
        db.commit()
        return True
    return False

#wet leaves
def create_wet_leaves(db: Session, wet_leaves: schemas.WetLeavesCreate):
    db_wet_leaves = models.WetLeaves(**wet_leaves.dict())
    db.add(db_wet_leaves)
    db.commit()
    db.refresh(db_wet_leaves)
    return db_wet_leaves
    
def get_wet_leaves(db: Session, limit: int = 100):
    return db.query(models.WetLeaves).limit(limit).all()

def get_wet_leaves_by_id(db: Session, wet_leaves_id: int):
    return db.query(models.WetLeaves).filter(models.WetLeaves.WetLeavesID == wet_leaves_id).first()

def delete_wet_leaves_by_id(db: Session, wet_leaves_id: int):
    wet_leaves = db.query(models.WetLeaves).filter(models.WetLeaves.WetLeavesID == wet_leaves_id).first()
    if wet_leaves:
        db.delete(wet_leaves)
        db.commit()
        return True
    return False

def update_wet_leaves(db: Session, wet_leaves_id: int, wet_leaves_update: schemas.WetLeavesUpdate):
    db_wet_leaves = db.query(models.WetLeaves).filter(models.WetLeaves.WetLeavesID == wet_leaves_id).first()
    if not db_wet_leaves:
        return None
    db_wet_leaves.Weight = wet_leaves_update.Weight
    if wet_leaves_update.Status:
        db_wet_leaves.Status = wet_leaves_update.Status
    db.commit()
    db.refresh(db_wet_leaves)
    return db_wet_leaves

def update_wet_leaves_status(db: Session, wet_leaves_id: int, status_update: schemas.WetLeavesStatusUpdate):
    db_wet_leaves = db.query(models.WetLeaves).filter(models.WetLeaves.WetLeavesID == wet_leaves_id).first()
    if not db_wet_leaves:
        return None
    db_wet_leaves.Status = status_update.Status
    db.commit()
    db.refresh(db_wet_leaves)
    return db_wet_leaves

# dry leaves
def create_dry_leaves(db: Session, dry_leaves: schemas.DryLeavesCreate):
    db_dry_leaves = models.DryLeaves(**dry_leaves.dict())
    db.add(db_dry_leaves)
    db.commit()
    db.refresh(db_dry_leaves)
    return db_dry_leaves

def get_dry_leaves(db: Session, limit: int = 100):
    return db.query(models.DryLeaves).limit(limit).all()

def get_dry_leaves_by_id(db: Session, dry_leaves_id: int):
    return db.query(models.DryLeaves).filter(models.DryLeaves.DryLeavesID == dry_leaves_id).first()

def delete_dry_leaves_by_id(db: Session, dry_leaves_id: int):
    dry_leaves = db.query(models.DryLeaves).filter(models.DryLeaves.DryLeavesID == dry_leaves_id).first()
    if dry_leaves:
        db.delete(dry_leaves)
        db.commit()
        return True
    return False

def update_dry_leaves(db: Session, dry_leaves_id: int, dry_leaves_update: schemas.DryLeavesUpdate):
    db_dry_leaves = db.query(models.DryLeaves).filter(models.DryLeaves.DryLeavesID == dry_leaves_id).first()
    if not db_dry_leaves:
        return None
    db_dry_leaves.Processed_Weight = dry_leaves_update.Weight
    if dry_leaves_update.Status:
        db_dry_leaves.Status = dry_leaves_update.Status
    db.commit()
    db.refresh(db_dry_leaves)
    return db_dry_leaves

def update_dry_leaves_status(db: Session, dry_leaves_id: int, status_update: schemas.DryLeavesStatusUpdate):
    db_dry_leaves = db.query(models.DryLeaves).filter(models.DryLeaves.DryLeavesID == dry_leaves_id).first()
    if not db_dry_leaves:
        return None
    db_dry_leaves.Status = status_update.Status
    db.commit()
    db.refresh(db_dry_leaves)
    return db_dry_leaves


#flour
def create_flour(db: Session, flour: schemas.WetLeavesCreate):
    db_flour = models.Flour(**flour.dict())
    db.add(db_flour)
    db.commit()
    db.refresh(db_flour)
    return db_flour
    
def get_flour(db: Session, limit: int = 100):
    return db.query(models.Flour).limit(limit).all()

def get_flour_by_id(db: Session, flour_id: int):
    return db.query(models.Flour).filter(models.Flour.FlourID == flour_id).first()

def delete_flour_by_id(db: Session, flour_id: int):
    flour = db.query(models.Flour).filter(models.Flour.FlourID == flour_id).first()
    if flour:
        db.delete(flour)
        db.commit()
        return True
    return False

def update_flour(db: Session, flour_id: int, flour_update: schemas.FlourUpdate):
    db_flour = db.query(models.Flour).filter(models.Flour.FlourID == flour_id).first()
    if not db_flour:
        return None
    db_flour.Flour_Weight = flour_update.Weight
    if flour_update.Status:
        db_flour.Status = flour_update.Status
    db.commit()
    db.refresh(db_flour)
    return db_flour

def update_flour_status(db: Session, flour_id: int, status_update: schemas.FlourStatusUpdate):
    db_flour = db.query(models.Flour).filter(models.Flour.FlourID == flour_id).first()
    if not db_flour:
        return None
    db_flour.Status = status_update.Status
    db.commit()
    db.refresh(db_flour)
    return db_flour

# shipment
def create_shipment(db: Session, shipment: schemas.ShipmentCreate):
    db_shipment = models.Shipment(**shipment.dict())
    db.add(db_shipment)
    db.commit()
    db.refresh(db_shipment)
    return db_shipment
    
def get_shipment(db: Session, limit: int = 100):
    return db.query(models.Shipment).limit(limit).all()

def get_shipment_by_id(db: Session, shipment_id: int):
    return db.query(models.Shipment).filter(models.Shipment.ShipmentID == shipment_id).first()

def delete_shipment_by_id(db: Session, shipment_id: int):
    shipment = db.query(models.Shipment).filter(models.Shipment.ShipmentID == shipment_id).first()
    if shipment:
        db.delete(shipment)
        db.commit()
        return True
    return False

def update_shipment(db: Session, shipment_id: int, shipment_update: schemas.ShipmentUpdate):
    # Query the shipment by its ID
    db_shipment = db.query(models.Shipment).filter(models.Shipment.ShipmentID == shipment_id).first()
    
    if not db_shipment:
        return None
    if shipment_update.CourierID is not None:
        db_shipment.CourierID = shipment_update.CourierID
    if shipment_update.FlourID is not None:
        db_shipment.FlourID = shipment_update.FlourID
    if shipment_update.ShipmentQuantity is not None:
        db_shipment.ShipmentQuantity = shipment_update.ShipmentQuantity
    if shipment_update.Check_in_Quantity is not None:
        db_shipment.Check_in_Quantity = shipment_update.Check_in_Quantity
    if shipment_update.Harbor_Reception_File is not None:
        db_shipment.Harbor_Reception_File = shipment_update.Harbor_Reception_File
    if shipment_update.Rescalled_Weight is not None:
        db_shipment.Rescalled_Weight = shipment_update.Rescalled_Weight
    if shipment_update.Centra_Reception_File is not None:
        db_shipment.Centra_Reception_File = shipment_update.Centra_Reception_File

    db.commit()
    db.refresh(db_shipment)
    return db_shipment


# location
def create_location(db: Session, location: schemas.LocationCreate):
    db_location = models.Location(**location.dict())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location
    
def get_location(db: Session, limit: int = 100):
    return db.query(models.Location).limit(limit).all()

def get_location_by_id(db: Session, location_id: int):
    return db.query(models.Location).filter(models.Location.LocationID == location_id).first()

def delete_location_by_id(db: Session, location_id: int):
    location = db.query(models.Location).filter(models.Location.LocationID == location_id).first()
    if location:
        db.delete(location)
        db.commit()
        return True
    return False