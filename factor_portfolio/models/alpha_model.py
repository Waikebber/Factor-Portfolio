"""
Alpha model implementation using machine learning.
"""

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LassoCV
from sklearn.preprocessing import StandardScaler

class AlphaModel:
    """Machine learning-based alpha model"""
    def __init__(self, model_type='random_forest'):
        """Initialize alpha model.
        
        Args:
            model_type (str): Type of model to use ('random_forest' or 'lasso')
        """
        self.model_type = model_type
        self.model = RandomForestRegressor(n_estimators=100) if model_type == 'random_forest' \
            else LassoCV(cv=5)
        self.scaler = StandardScaler()
    
    def fit(self, X, y):
        """Train the model.
        
        Args:
            X (pd.DataFrame): Feature matrix
            y (pd.Series): Target variable
            
        Returns:
            self: Trained model
        """
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        return self
    
    def predict(self, X):
        """Generate predictions.
        
        Args:
            X (pd.DataFrame): Feature matrix
            
        Returns:
            np.array: Predicted values
        """
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled) 